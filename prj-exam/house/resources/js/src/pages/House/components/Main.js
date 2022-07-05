import {memo, useCallback, useEffect, useState} from "react";
import {Product} from "../../../components/Product";
import {Sidebar} from "./Sidebar";
import {useDispatch, useSelector} from "react-redux";
import {getProductAction} from "../../../service/redux";

export const Main = memo(({handleChangePage})=>{
    const [pageFocus, setPageFocus] = useState("");
    const dispatch = useDispatch();
    const current_page = useSelector((state)=>state.house.products.current_page)
    const last_page = useSelector((state)=>state.house.products.last_page)
    const data = useSelector((state)=> state.house.products.data);
    const pages = useSelector((state)=>state.house.products.links);

    const onClickPage = useCallback((url, label)=>{
        setPageFocus(label)
        handleChangePage(url)
    },[pageFocus])

    useEffect(()=>{dispatch(getProductAction("/api/houses"))},[])

    return(
        <div className="main">
            <div className="header-main">
                {current_page && "Trang: "+ current_page+"/ "+ last_page +" trang"}
            </div>
            <div className="content-main">
                {data && data.map((item, index)=><Product item={item} key={index}/>)}
            </div>
            <div className="pages">
                {pages && pages.map((item, index)=>
                        <button className={item.label == pageFocus ? "btn btn-danger": "btn page btn-primary"} key={index}
                                onClick={()=>onClickPage(item.url, item.label)}>
                            {item.label.includes("Previous")?"Previous" : item.label.includes("Next") ? "Next" : item.label}
                        </button>
                  )}
            </div>
    </div>)
})
