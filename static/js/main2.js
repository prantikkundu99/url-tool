console.log("JS Loaded");
let copyBtn = document.getElementById("copybutton");
let copyPass = document.getElementById("copypass");
let successAlert = document.getElementById("success-alert");
let alertText = document.getElementById("alerttext");

if (copyBtn){
    copyBtn.addEventListener('click',(event)=>{
        navigator.clipboard.writeText(event.target.dataset.pass);
        if (successAlert){
            successAlert.classList.remove("d-none");
            successAlert.classList.add("d-flex");
            alertText.innerText = "Password successfully copied!"
        }

    })
}       