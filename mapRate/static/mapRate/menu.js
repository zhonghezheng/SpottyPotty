document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#bMap').addEventListener('click', () => load_map('map'));
    document.querySelector('#aMap').addEventListener('click', () => load_map('add'));
    document.querySelector('#rMap').addEventListener('click', () => load_map('rate'));
    console.log("here");
    load_map('map'); //default
});

function load_map(status){
    document.querySelector('#map').style.display = 'none';
    document.querySelector('#add').style.display = 'none';
    document.querySelector('#rate').style.display = 'none';
    stat = "#".concat(status);
    console.log(stat);
    document.querySelector(stat).style.display = 'block';

}