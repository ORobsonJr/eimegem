
function showResult() {
    /* 
    This function receive an image and return a text

    The process work in the following way:
    1. Receive the image uploaded
    2. Convert to Base64 and send to backend
    3. Backend process the image and return a reponse
    4. We pass the response from server to client


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
            const supportMediaTypes = ["image/png", "image/jpeg", "image/jpg"];
            
            if (supportMediaTypes.indexOf(file['type']) ==-1){
                console.log(file['type']);
                alert('Formato de arquivo não permitido');
                return 
            }
            
            const endpoint = "http://localhost:8000/v1/convertImage"

            var xhr = new XMLHttpRequest();
            xhr.open("POST", endpoint);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(JSON.stringify({"data": reader.result}));
            
            xhr.onreadystatechange = function () {
                dataJSON = JSON.parse(xhr.response)
                if (dataJSON.hasOwnProperty('data')) {
                    document.getElementById('output-text').value = dataJSON["data"];
                }

                else if (dataJSON["erro"]) {
                    alert(dataJSON['erro']);
                }

                else {
                    alert("Erro while try to use 'data' key value :" + dataJSON);
                }
                } 
        });
        reader.readAsDataURL(file);
    });
};


    
        





    
    
    
