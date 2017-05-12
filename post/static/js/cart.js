$(document).ready(function () {
    $('button').click(function () {
        var count=0


        if($(this).attr('class')=="minus-ll" ){

            count=-1;


        }
        if($(this).attr('class')=="plus-ll" ) {

            count=+1;



            }
                $.ajax({
                    url:'/shopping_cart',
                    type:'post',
                    data:{id:$(this).attr('id'),changecount:count},
                    success:function (quantity) {
                        $("num").text();

                    }
                })
            });

});
