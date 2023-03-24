
function showResult() {
    /* 
    This function receive a text image and return a text string

    The process work in the following way:
    1. Receive the image uploaded
    2. Convert to Base64 and send to backend
    3. Backend process the image and return a reponse
    4. We passed the response from server to client
    */
    const fileInput = document.getElementById('button-file');

    fileInput.addEventListener("change", e => {
        const file = fileInput.files[0];
        const reader = new FileReader();

        console.log(file);
        //Clear the ouput before we add another value.
        document.getElementById('output-text').value = "";


        reader.addEventListener("load", () => {
            /*
            Send base64 data to api
            */

            //We make a filter in html and js to filter extensions types
            const supportMediaTypes = ["image/png", "image/jpeg", "image/jpg", "application/pdf"];
            
            const IndexFileType = supportMediaTypes.indexOf(file['type'])
            if (supportMediaTypes.indexOf(file['type']) !=-1){
                /*
                Return file extension
                */  

                var item = supportMediaTypes[IndexFileType]; //The item from list
                var findSlash = item.indexOf('/')
                const fileType = item.slice(findSlash+1, item.length)
                
                

                const endpoint = "http://localhost:8000/v1/convertImage"

                var xhr = new XMLHttpRequest();
                xhr.open("POST", endpoint);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({"data": reader.result, "dataType": fileType}));
                xhr.onreadystatechange = function () {
                    dataJSON = JSON.parse(xhr.response)
                    if (dataJSON.hasOwnProperty('data')) {
                        document.getElementById('output-text').value = dataJSON["data"];
                    }

                    else if (dataJSON["erro"]) {
                        alert("Aconteceu um erro", dataJSON['erro']);
                        console.log(dataJSON);

                    }

                    else {
                        alert("Erro while try to use 'data' key value :" + dataJSON);
                    }
                    } 
            }
            

            else{
                console.log(file['type']);
                alert('Formato de arquivo não permitido');
            }
            

            
            fileInput.reset();
            
        });
        reader.readAsDataURL(file);
    });
};


    
        





    
    
    
