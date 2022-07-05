import {getProduct, postProduct} from "./api";
import { combineReducers, createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import thunk from 'redux-thunk';

const GET_PRODUCT = "product"
const GET_PRICE = "price"
const initProduct = {
    products:{},
    price:0,
}
export const requestSuccess = (data, type)=>{
    return {
        data : data,
        type : type,
    }
}

const productReducer = (state = initProduct, action) =>{
    switch (action.type){
        case GET_PRODUCT :
            return {
                ...state,
                products: action.data,
            }
        case GET_PRICE :
            return {
                ...state,
                price: action.data,
            }
        default:
            return state;
    }
}

export const getProductAction = (url) => {
    return async dispatch => {
        const server = "http://localhost:8000";
        const res = await getProduct(url, server)
        dispatch(requestSuccess(res ,GET_PRODUCT));
    }
}

export const postProductAction = (url, data) => {
    return async dispatch =>{
        const server = "http://localhost:8000";
        const res = await postProduct(url, server, data)
        dispatch(requestSuccess(res ,GET_PRODUCT));
    }
}

export const postPriceAction = (url, data)=> {
    return async dispatch => {
        const server = "https://b7e1-35-239-77-122.ngrok.io";
        const res = await postProduct(url, server, data)
        dispatch(requestSuccess(res, GET_PRICE));
    }
}

const reducer = combineReducers(
    {
        house: productReducer
    }
)
const store = createStore(reducer, composeWithDevTools(applyMiddleware(thunk)));

export default store
