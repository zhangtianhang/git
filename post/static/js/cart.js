$(document).ready(function () {
    $('button').click(function () {
        var id=$(this).attr('id')
        var count = 0
        if ($(this).attr('class') == "minus-ll") {
            count = -1;
        }
        if ($(this).attr('class') == "plus-ll") {
            var id = $(this).attr('id');
            count = +1;

        }
        $.ajax({
            url: '/shopping_cart',
            type: 'post',
            data: {id: $(this).attr('id'), changecount: count},
            success: function (result) {
                $("#"+id).parent().siblings().find('span').text(result.sub_count);
                console.log($("#"+id).parent().siblings().find('span'))
                $("#"+id).parent().parent().parent().siblings().find('numbr').text(result.subtotal)

            }
        })
    })
})

