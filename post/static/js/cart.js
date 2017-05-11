$(document).ready(function () {
    $('button').click(function () {
        var count=0
        if(this.class='minus-ll'){
            count=-1;
            return count
        }
        if(this.class='plus-ll') {
                count+= 1;
                return count
            }
                $.ajax({
                    url:'/shopping_cart',
                    type:'post',
                    data:{id:$(this).attr('id'),changecount:count},
                    success:function (sum_count) {

                    }
                })
            });

});
