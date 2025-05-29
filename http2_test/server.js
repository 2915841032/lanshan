const http2 = require('http2');
const fs = require('fs');

// 读取 SSL 证书和密钥
const options = {
    key: fs.readFileSync('localhost-privkey.pem'),
    cert: fs.readFileSync('localhost-cert.pem')
};

// 创建 HTTP/2 服务器
const server = http2.createSecureServer(options, (req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello, HTTP/2!');
});

// 监听端口
server.listen(8443, () => {
    console.log('HTTP/2 server is listening on https://localhost:8443');
});
