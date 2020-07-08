function onFind() {
    /*TODO: make find requests*/
    $.ajax({
        type: "POST",
        url: '/api/tariff_search',
        data: {'query': document.getElementById('treatment').value},
        success: function (e) {
            console.log(e.results)
        }
    })
}

$('#list-tab a').on('click', function (e) {
    /*TODO: tarif show*/
    console.log(e.target.name)
})