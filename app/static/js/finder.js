document.getElementById('treatment').addEventListener("input", onFind)
document.getElementById('treatment').addEventListener("submit", onFind)


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
    $.ajax({
        type: "POST",
        url: '/api/get_tariff',
        data: {'tariff_id': tariff_id},
        success: function (e) {
            document.getElementById('tariff_code').innerText = e.result[0].tariff_code;
            document.getElementById('tariff_text').innerText = e.result[0].treatment;
            document.getElementById('treatment_price').innerText = e.result[0].tariff;

            document.getElementById('tariff_info').style.display = 'flex'

            $('html, body').animate({
                scrollTop: $("#tariff_text").offset().top
            }, 1000);
        }
    })
}