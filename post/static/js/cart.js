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
                if(result.count==0){
                    $("#"+id).parent().parent().parent().parent().detach()
                }
                 $("number").text(result.sum_count)
                $("#"+id).parent().siblings().find('span').text(result.sub_count);

                    $("#"+id).parent().parent().parent().siblings().find('numbr').text(result.subtotal)

                    $("#"+id).parent().parent().parent().siblings().find('num').text(result.costprice)


            }
        })
    })
})

