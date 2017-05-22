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
                if(result.sub_count==0){
                    $("#"+id).parent().parent().parent().parent().detach()
                }
                $("#"+id).parent().siblings().find('span').text(result.sub_count);

                if(result.subtotal==result.costprice){
                    $("#"+id).parent().parent().parent().next().text(result.subtotal.toFixed(1)+'元')

                }else{
                    $("#"+id).parent().parent().parent().next().text(result.subtotal.toFixed(1)+'元'+'(原价:'+result.costprice.toFixed(1)+'元)')

                }
                $("number").text(result.sum_count)
                if(result.sum_count==0){
                    location.href = '/shopping_list';
                }
                 $("num").text(result.total)




            }
        })
    })

})

