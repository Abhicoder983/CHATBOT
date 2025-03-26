function registration(){
    var name = document.getElementById('Name').value;
    var password = document.getElementById('Password').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('roll_no').value;
    if(name===""|| password===""|| phone==="" || email===""){
    alert('all field are required to field');
    return false;
    }
    var nameRegex = /^[A-Za-z\s]+$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!nameRegex.test(name)){
    alert('Please enter the valid name');
    return false;
    }
    if (password.length<8){
    alert('Password should be more than 8 character');
    return false;
    }
    if(!emailRegex.test(email)){
        alert('enter the valid email id');
        return false;
    }
    if(phone.length>10){
        alert('enter the valid number');
        return false;
    }

    return true;
}