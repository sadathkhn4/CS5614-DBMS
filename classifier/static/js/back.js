

function resultGenerate() {
    console.log("Hey!");

    var container = document.getElementById("imageContainer");

        // Create and display the div
        container.style.display = "block";

        // Create and append 5 images to the div
        for (var i = 1; i <= 5; i++) {
            var image = document.createElement("img");

            //image.src = "https://www.operationkindness.org/wp-content/uploads/blog-kitten-nursery-operation-kindness.jpg";  // Replace with your actual image paths
            var path_src = 'img/0' + i + '.jpg';
            //image.src = "{% static path_src %}";
            image.src = "{% static '../img/02.jpg' %}"
            image.alt = "Image_0 " + i;
            image.classList.add("image");
            container.appendChild(image);
        }
}