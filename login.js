document.getElementById("login").onclick = function (e) {
    e.preventDefault();

    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    if (email == "" || email == "") {
        document.getElementById("msg").innerHTML = "Niste popunili potrebna polja";
    }

    if (email != "" || email != "") {
        fetch("http://localhost:8080/login", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            }),
        })
            .then((response) => response.json())
            .then((result) => {
                if (result["msg"]) {
                    document.getElementById("msg").innerHTML = result["msg"];
                } else {
                    document.getElementById("msg").innerHTML = "Uspješna prijava.";
                    sessionStorage.setItem('user', JSON.stringify(result));

                    email = "";
                    password = "";
                    
                    if (result["usertype"] == 1) {
                        window.location.href = "students.html";
                    } else {
                        window.location.href = "profesors.html";
                    }
                }
            });
    }

}