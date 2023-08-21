if (!sessionStorage.user) {
    window.location.href = "/";
}

user = JSON.parse(sessionStorage.user);
document.getElementById("name").innerHTML = user["name"];

document.getElementById("logout").onclick = function (e) {
    e.preventDefault();

    sessionStorage.removeItem("user");
    sessionStorage.removeItem("courseid");
    window.location.href = "/";    
}

function showCourse(link, courseid) {
    sessionStorage.setItem('courseid', courseid);
    window.location.href = link;  
}

fetch("http://localhost:8080/studentscourses/student/" + user["id"], {
    method: "GET",
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    },
})
    .then((response) => response.json())
    .then((result) => {
        for (var item of result["studentscourses"]) {
            document.getElementById("list").innerHTML += "<li><strong>Predmet:</strong><a href=\"javascript:showCourse('" + item["link"] + "', " + item["courseid"] + ");\">" + item["coursename"] + "</li>";
        }
    });

