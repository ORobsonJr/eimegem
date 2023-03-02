
function showResult() {
    const fileInput = document.getElementById('file-input-element');

    fileInput.addEventListener("change", e => {
        const file = fileInput.files[0];
        const reader = new FileReader();

        reader.addEventListener("load", () => {
            // Base64 Data URL 👇
            console.log(reader.result);
        });

        reader.readAsDataURL(file);
    });




};


    
        





    
    
    
