document.addEventListener("DOMContentLoaded", function (e){
        options = document.getElementsByClassName("hyperlink");

        for (let i = 0; i < options.length; i++) {
            options[i].addEventListener("click", function (){
                document.location = document.location.origin + "/" + options[i].id;
            });
        }
    }
    );