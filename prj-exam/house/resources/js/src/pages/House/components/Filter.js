import {memo, useEffect} from "react";
import data from "../../../service/data_select.json";
import {Select} from "./Select";
import {useDispatch} from "react-redux";
import {postProductAction} from "../../../service/redux";
import ICSearch from "../../../../../../public/image/icon/search.png"

export const Filter = memo(({handleSubmit, handleChangeDataFilter, dataFilter})=>{
    return(
        <div className="filter">
            <form className="form" onSubmit={handleSubmit}>
                <div className="search">
                    <input type= "text"placeholder="search for title " className="form-control" value={dataFilter["title"]}
                           onChange={(event)=>handleChangeDataFilter("title", event.target.value)}/>
                </div>
                <Select name="Mức giá" data={data.price} defaultValue = {0} onChange={handleChangeDataFilter} keyName="price"/>
                <Select name="Diện tích"data={data.square} defaultValue = {0} onChange={handleChangeDataFilter} keyName="square"/>
                <Select name="Hướng nhà" data={data.direct} defaultValue = "" onChange={handleChangeDataFilter} keyName="direct"/>
                <Select name="Thành phố" data={data.province} defaultValue= "" onChange={handleChangeDataFilter} keyName="province"/>

                <button className="btn btn-primary btn-search" type="submit">
                    <i className="bi bi-search"></i>
                    <div>Tìm kiếm</div>
                </button>
            </form>
    </div>)
})
