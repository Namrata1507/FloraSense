const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");
const uploadStateEmpty = document.getElementById("uploadStateEmpty");
const uploadStatePreview = document.getElementById("uploadStatePreview");
const btnDetect = document.getElementById("btnDetect");

imageInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        previewImage.src = URL.createObjectURL(file);
        uploadStateEmpty.style.display = "none";
        uploadStatePreview.style.display = "block";
        btnDetect.disabled = false;
    }
});

function removeImage() {
    imageInput.value = "";
    uploadStateEmpty.style.display = "block";
    uploadStatePreview.style.display = "none";
    btnDetect.disabled = true;
}

async function detectPlant() {

    const fileInput = document.getElementById("imageInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    // show result panel
    document.getElementById("resultBox").style.display = "block";

    // update plant name
    document.getElementById("resName").innerText = "Detected Plant";

    // update category
    const category = document.getElementById("resCategory");
    category.innerText = data.plant_type;

    if (data.plant_type === "Invasive") {
        category.classList.add("danger");
    } else {
        category.classList.add("success");
    }

    // confidence demo value
    document.getElementById("resConfBar").style.width = "85%";
    document.getElementById("resConfText").innerText = "85%";
}
