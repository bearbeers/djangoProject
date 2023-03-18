function isSatisfactory(){
    let email = document.getElementById('inputEmail3').value;
    let pwd = document.getElementById('inputPassword3').value;
    let pwd2 = document.getElementById('PasswordAgain').value;
    let phoneNumber = document.getElementById('PhoneNumber').value;
    if(email.includes('@') === false){
        alert('Please enter the correct email address!')
        return false
    }else if(pwd.length < 6){
        alert('The password length does not meet the requirements！')
        return false
    }else if(pwd !== pwd2){
        alert('The passwords entered twice do not match！')
        return false
    }else if(phoneNumber.length !== 11 || phoneNumber.substring(0,2) === '123' || phoneNumber.substring(0,2) ==='110'){
        alert('Please enter the correct phone number')
        return false
    }else if(email === ''||pwd===''||pwd2===''||phoneNumber===''){
        alert('Please enter this info')
        return false
    }
    return true
}