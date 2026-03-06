function uploadImage() {

let fileInput = document.getElementById("imageInput");

if (fileInput.files.length === 0) {
    alert("Please select an image first");
    return;
}

let file = fileInput.files[0];

let formData = new FormData();
formData.append("image", file);

fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
})
.then(response => response.json())
.then(data => {
    document.getElementById("result").innerText =
    "Prediction: " + data.prediction;
})
.catch(error => {
    console.log(error);
});

}