import {memo, useCallback, useState} from "react";
import {Header} from "./components/Header";
import {Filter} from "./components/Filter";
import {Main} from "./components/Main";
import {Sidebar} from "./components/Sidebar";
import {getProductAction, postPriceAction, postProductAction} from "../../service/redux";
import {useDispatch} from "react-redux";

export const House = memo(()=>{
    const dispatch = useDispatch()
    const [dataFilter, setDataFilter] = useState({
        "title": "",
        "price": 0,
        "square": 0,
        "direct": "",
        "province":""
    })

    const handleChangeDataFilter= useCallback((keyName, value)=>{
        setDataFilter((state)=>{return {
            ...state,
            [keyName]: value
        }})

    },[dataFilter.keyName])

    const handleSubmit = useCallback((event)=>{
        event.preventDefault()
        dispatch(postProductAction("api/filter/houses", dataFilter))
    },[dataFilter])

    const handleChangePage = useCallback((url)=>{
        if(url.includes("/filter")){
            dispatch(postProductAction(url, dataFilter))
        }
        else{
            dispatch(getProductAction(url))
        }
    },[dataFilter])

    return (
        <div className="house" >
            <Header/>
            <Filter
                dataFilter = {dataFilter}
                handleChangeDataFilter= {handleChangeDataFilter}
                handleSubmit={handleSubmit}
                handleChangePage={handleChangePage} />
            <div className="content">
                <Main handleChangePage = {handleChangePage}/>
                <Sidebar/>
            </div>
        </div>
    )
})

