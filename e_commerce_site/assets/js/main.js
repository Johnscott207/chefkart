
document.querySelectorAll(".product_detail .varints .btns").forEach(val=>{

    var inp = val.querySelector("input");
            if(!inp.checked){     
                val.classList.remove("varaintchk");
                val.classList.add("varaint");
            }else{
                val.classList.remove("varaint");
                val.classList.add("varaintchk");
            }
  
    val.onclick=function(){
        this.querySelector("input").checked=true;
        this.classList.remove("varaint");
        this.classList.add("varaintchk");
        document.querySelectorAll(".product_detail .varints .btns").forEach(vl=>{
            var inp = vl.querySelector("input");
                if(!inp.checked){     
                    vl.classList.remove("varaintchk");
                    vl.classList.add("varaint");
                }
            
        });
    };
});

document.querySelectorAll(".product_detail .colors .btns").forEach(val=>{
        var inp = val.querySelector("input");
            if(!inp.checked){     
                val.classList.remove("varaintchk");
                val.classList.add("color");
                val.style.background = "#f0f0f0";
            }else{
                val.classList.remove("color");
                val.classList.add("varaintchk");
                val.style.background = val.textContent;
            }
        
  
    val.onclick=function(){
        this.querySelector("input").checked=true;
        this.classList.remove("color");
        this.classList.add("varaintchk");
        this.style.background = this.textContent;
        document.querySelectorAll(".product_detail .colors .btns").forEach(vl=>{
            var inp = vl.querySelector("input");
                if(!inp.checked){     
                    vl.classList.remove("varaintchk");
                    vl.classList.add("color");
                    vl.style.background = "#f0f0f0";
                }
            
        });
    };
});