

//Función que llama a las validaciones del CommentForm
function setUpCommetsForm(event){
    let ids=["content","title-comment"]
     for(i=0 ;i<ids.length;i++){
        validateEmpty(ids[i],event)
    }
}


//Función que llama a las validaciones del RecipeForm
function setUpRecipeForm(event){
    let ids=["rtitle","rpreparacion","ringredientes"]
    for(i=0 ;i<ids.length;i++){
        validateEmpty(ids[i],event)
    }
}

//Valida si un campo es vacío y en caso afirmativo evita el submit del formulario mostrando un error
function validateEmpty(item,event) {
    let toValidate=document.getElementById(item)
    if (toValidate.value.length=== 0)
    {
        toValidate.style.border="red";
        toValidate.style.borderStyle="solid";
        event.preventDefault()

        alert("Los campos resaltados no se permiten en blanco")
        return false;
    }else {
        return true
    }
}

