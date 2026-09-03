
document.addEventListener("DOMContentLoaded",()=>{
 const b=document.querySelector(".menu"), l=document.querySelector(".links");
 if(b&&l) b.addEventListener("click",()=>l.classList.toggle("open"));
 document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener("click",()=>l&&l.classList.remove("open")));
});
