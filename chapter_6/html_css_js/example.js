
function get_cat_fact(domId) {
    fetch("https://catfact.ninja/fact")
    .then(response => response.json())
    .then(data => document.getElementById(domId).innerHTML = data.fact);
}
