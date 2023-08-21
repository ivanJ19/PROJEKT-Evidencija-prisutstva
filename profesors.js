if (!sessionStorage.user) {
    window.location.href = "/";
}

user = JSON.parse(sessionStorage.user);
document.getElementById("name").innerHTML = user["name"];

fetch("http://localhost:8080/profesorscourses/profesor/" + user["id"], {
    method: "GET",
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
})
    .then((response) => response.json())
    .then((result) => {
        document.getElementById("course").innerHTML = result["coursename"];
    });

fetch("http://localhost:8080/login/hour", {
    method: "GET",
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
})
    .then((response) => response.json())
    .then((result) => {
        for (var item of result["logins"]) {
            document.getElementById("list").innerHTML += "<li><strong>Ime studenta:</strong> " + item["name"] + ", <strong>Email adresa:</strong> " + item["email"] + ", <strong>Datum prijave:</strong> " + item["logindate"] + "</li>";
        }
    });

document.getElementById("logout").onclick = function (e) {
    e.preventDefault();

    sessionStorage.removeItem("user");
    sessionStorage.removeItem("courseid");
    window.location.href = "/";
}