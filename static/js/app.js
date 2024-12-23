function check() {
    let year = document.getElementById("year").value;
    let leap = document.getElementById("leap_print");
    console.log(leap);
    let url = "http://127.0.0.1:5000/leap";

    $.post(url,
        { year: year },  
        function (data, status) {
            console.log(data);
            leap.innerHTML = data.year;
        })
}
