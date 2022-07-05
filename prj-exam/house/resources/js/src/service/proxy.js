import {createProxyMiddleware} from "http-proxy-middleware";

module.exports = app =>{
    app.use(
        createProxyMiddleware("/predict"),
        {
            target: 'https://24d6-34-134-22-164.ngrok.io',
            changeOrigin:true,
        }
    )
}
