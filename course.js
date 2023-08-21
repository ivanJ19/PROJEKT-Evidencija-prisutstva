if (!sessionStorage.user) {
    window.location.href = "/";
}

user = JSON.parse(sessionStorage.user);
courseid = sessionStorage.courseid
document.getElementById("name").innerHTML = user["name"];

document.getElementById("back").onclick = function (e) {
    e.preventDefault();

    window.location.href = "/students.html";    
}

document.getElementById("logout").onclick = function (e) {
    e.preventDefault();

    sessionStorage.removeItem("user");
    sessionStorage.removeItem("courseid");
    window.location.href = "/";    
}

fetch("http://localhost:8080/studentscourses/course/" + user["id"] + "/" + courseid, {
    method: "GET",
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
})
    .then((response) => response.json())
    .then((result) => {
        document.getElementById("course").innerHTML = result["coursename"];
        document.getElementById("description").innerHTML = result["description"];
        document.getElementById("grade").innerHTML = result["grade"];
    });