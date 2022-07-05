import {memo} from "react";
import IMGBANNER from "../../../../../../public/image/logo/banner.png"

export const Header = memo(()=>{
    return (<div className="header">
        <img src={IMGBANNER} />
    </div>)
})
