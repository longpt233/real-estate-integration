import {memo, useCallback, useState} from "react";
import {useDispatch, useSelector} from "react-redux";
import {postPriceAction} from "../../../service/redux";
import {standardPrice} from "../../../service/standardPrice";

export const Sidebar = memo(()=>{
    const price = useSelector((state)=>state.house.price);
    const dispatch = useDispatch()
    const [dataPredict, setDataPredict] = useState({
        "square":"",
        "floor":"",
        "bedroom":"",
        "district": "",
        "ward":"",
        "province":""
    });

    const handlePredict = useCallback(()=>{
        event.preventDefault();
        const data = {
            ...dataPredict,
            "district": [dataPredict.district],
            "ward": [dataPredict.bedroom],
            "province": [dataPredict.province]
        }

        console.log(data)
        dispatch(postPriceAction("/predict",data));
    },[dataPredict]);

    const changeDataPredict = useCallback((keyName, value)=>{
        setDataPredict((state)=>{return {
            ...state,
            [keyName]:value,
        }})
    },[dataPredict.keyName])

    return (<div className="sidebar">
        <h1 className="title-sidebar">Dự đoán giá nhà</h1>
            <form onSubmit={handlePredict}>
                <div className="content-sidebar">
                    <div className="left ">
                        <div className="predict">
                            <label>Diện tích (m2)<span className="required">*</span> : </label>
                            <input type="number" min="0" className="form-control" required={true} value={dataPredict["square"]}
                                   onChange={(event)=>changeDataPredict("square", event.target.value)}/>
                        </div>
                        <div className="predict">
                            <label>Số tầng (tầng)<span className="required">*</span> : </label>
                            <input type="number" min="0" className="form-control" required={true} value={dataPredict["floor"]}
                                   onChange={(event)=>changeDataPredict("floor", event.target.value)} />
                        </div>
                        <div className="predict">
                            <label>Phòng ngủ (phòng)<span className="required">*</span> : </label>
                            <input type="number" min="0" className="form-control" required={true} value={dataPredict["bedroom"]}
                                   onChange={(event)=>changeDataPredict("bedroom", event.target.value)}/>
                        </div>
                    </div>
                    <div className="right">
                        <div className="predict">
                            <label>Tỉnh/Thành phố<span className="required">*</span> : </label>
                            <input type="text" className="form-control" required={true} value={dataPredict["province"]}
                                   onChange={(event)=>changeDataPredict("province", event.target.value)}/>
                        </div>
                        <div className="predict">
                            <label>Quận/Huyện<span className="required">*</span> : </label>
                            <input type="text" className="form-control" required={true} value={dataPredict["district"]}
                                   onChange={(event)=>changeDataPredict("district", event.target.value)}/>
                        </div>
                        <div className="predict">
                            <label>Phường/Xã<span className="required">*</span> : </label>
                            <input type="text" className="form-control" required={true} value={dataPredict["ward"]}
                                   onChange={(event)=>changeDataPredict("ward", event.target.value)}/>
                        </div>
                    </div>
                </div>
                <button className="btn btn-primary" type="submit"> Dự đoán </button>
            </form>
        <div className="result"><label>Kết quả dự đoán: {price && standardPrice(price.prediction[0])} đồng</label></div>
    </div>)
})
