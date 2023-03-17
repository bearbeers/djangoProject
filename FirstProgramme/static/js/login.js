function isInputEmailPassWord() {
    let email = document.getElementById("inputEmail3").value;
    let password = document.getElementById("inputPassword3").value;
    console.log(email);
    console.log(password);
    if (email.length === 0 || password.length === 0) {
        alert("Please input your email and password!");
        return false;
    }
    return true;
}