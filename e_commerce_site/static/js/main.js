
document.querySelectorAll(".product_detail .btns").forEach(val=>{
  
    val.onclick=function(){
        this.querySelector("input").checked=true;
        this.classList.remove("varaint");
        this.classList.add("varaintchk");
        document.querySelectorAll(".product_detail .btns").forEach(vl=>{
            var inp = vl.querySelector("input");
                if(!inp.checked){     
                    vl.classList.remove("varaintchk");
                    vl.classList.add("varaint");
                }
            
        });
    };
});