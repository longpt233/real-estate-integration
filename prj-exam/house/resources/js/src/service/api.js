import axios from 'axios';

// axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
// axios.defaults.headers.common['Accept'] = 'application/json';

const axiosClient = (method, url, server, data={}) => {
    const headers={"Access-Control-Allow-Origin": "*"}
    return axios({
        method: method,
        baseURL: server,
        url: url,
        data: data,
        headers:headers,
    })
};

export default axiosClient;


export const getProduct = async (url, server)=>{
    try{
        const promise = await axiosClient("get",url, server).
        then((response) => response.data)
        return promise

    } catch(error){
        console.log(error)
    }
}

export const postProduct = async (url, server, data)=>{
    try{
        const promise = await axiosClient("post", url, server, data).
        then((response) => response.data)
        return promise

    } catch(error){
    }
}
