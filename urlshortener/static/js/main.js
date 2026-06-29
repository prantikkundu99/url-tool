let copyUrl = document.getElementById("copyurl");
let successAlert = document.getElementById("success-alert");
let alertText = document.getElementById("alerttext");

if (copyUrl){
    copyUrl.addEventListener('click',(event)=>{
        navigator.clipboard.writeText(event.target.dataset.url);
        if (successAlert){
            successAlert.classList.remove("d-none");
            successAlert.classList.add("d-flex");
            alertText.innerText = "Url successfully copied!"
        }

    })
}       