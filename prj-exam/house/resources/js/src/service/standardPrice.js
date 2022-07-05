
export const standardPrice= (price)=>{
    if(price == "None"){
        return "__"
    }
    else {
        const bilion = price/1000000000
        if (bilion > 1){
            return bilion.toFixed(2) +" tỷ"
        }
        else {
            const milion = price/1000000
            if(milion > 100)
                return milion.toFixed(2) +" triệu"
            else{
                if(milion<100 && milion >1){
                    return milion.toFixed(2) + " triệu/m2"
                }
                else{
                    return price.toFixed(2) + " đồng"
                }
            }
        }
    }
}
