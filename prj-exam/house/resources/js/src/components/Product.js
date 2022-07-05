import {memo, useCallback} from "react";
import ICBedroom from "../../../../public/image/icon/bedroom.png"
import ICParking from "../../../../public/image/icon/parking.png"
import ICFloor from "../../../../public/image/icon/floor.png"
import ICKitchen from "../../../../public/image/icon/kitchen.png"
import {standardPrice} from "../service/standardPrice";

export const Product = memo(({item})=>{
    return(<div className="item">
            <img src={item.link_image} alt="not found" />
            <div className="content-item">
                <div className="title">
                    <a href={item.url_page}><div className="text">{item.title}</div></a>
                </div>
                <div className="wrapper-square-direct">
                    <div className="square">
                        <label>Diện tích: </label>
                        {item.square=="None" ? "__":item.square+" m"}
                    </div>

                    <div className="size">
                        <label >Kích thước: </label>
                        {item.width && item.length && item.width+"x"+item.length}
                    </div>
                    <div className="direct">
                        <label >Hướng: </label>
                        {item.direct=="None" ? "__": " "+item.direct}
                    </div>
                </div>
                <div className="wrapper-price-location">
                    <div className="price">
                        <label >Giá :</label>
                        {standardPrice(item.price)}
                    </div>
                    <div className="jurial">
                        <label >Pháp lý :</label>
                        {item.juridical}
                    </div>
                    <div className="address">
                        <label>Địa chỉ :</label>
                        {item.street=="None"?"": " Đường " + item.street+"," }
                        {item.ward=="None"?"": " Phường " +item.ward+"," }
                        {item.district=="None"?"": " Quận " +item.district+"," }
                        {item.province=="None"?"": " Thành phố " + item.province }
                    </div>
                </div>
                <div className="wrapper-bedroom-parking-floor">
                    <div className="bedroom ic">
                        <img className="icon" src={ICBedroom}/>
                        <div>{item.bedroom == "" ? "__" : item.bedroom.replace("pn", "phòng ngủ")}</div>
                    </div>
                    <div className="kitchen ic">
                        <img className="icon" src={ICKitchen}/>
                        <div>{item.kitchen == "" ? "__" :item.kitchen + " phòng bếp"}</div>
                    </div>

                    <div className="parking ic">
                        <img className="icon" src={ICParking}/>
                        <div>{item.parking == "" ? "__" :item.parking+" chỗ để xe"}</div>
                    </div>

                    <div className="floor ic">
                        <img className="icon" src={ICFloor}/>
                        <div>{item.floor == "" ? "__" : item.floor.replace("t", "tầng")}</div>
                    </div>

                </div>
                <div className="wrapper-upload">
                    <div className="date">
                        <label>Ngày đăng: </label>
                        {" "+item.date}
                    </div>
                    <div className="name_contact">
                        <label>Người đăng : </label>
                        {item.name_contact == "" ? " __": " "+item.name_contact}
                    </div>
                </div>

            </div>
        </div>)
})
