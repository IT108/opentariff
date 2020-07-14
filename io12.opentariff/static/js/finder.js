function onFind() {
    $.ajax({
        type: "POST",
        url: '/api/tariff_search',
        data: {'query': document.getElementById('treatment').value},
        success: function (e) {
            document.getElementById('list-tab').innerHTML = e;
            $('#list-tab a').on('click', function (e) {
                select_tariff(e.target.name)
            })
        }
    })
}

function select_tariff(tariff_id) {
    console.log(tariff_id)
    document.getElementById('treatment').value
}