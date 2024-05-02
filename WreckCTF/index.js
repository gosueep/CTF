// [FLAG REDACTED]

const http = require('http')
const path = require('path')
const url = require('url')
const fs = require('fs')

const mime = new Map([
    ['html', 'text/html'],
    ['css', 'text/css'],
    ['js', 'text/javascript'],
    ['json', 'application/json'],
    ['png', 'image/png'],
    ['jpg', 'image/jpg'],
])


const handler = async (req, res) => {
    let filePath = path.join('public', url.parse(req.url).pathname)
    if (filePath.endsWith('/')) {
        filePath = path.join(filePath, 'index.html')
    }
    const type = mime.get(path.extname(filePath).slice(1)) || 'text/plain'

    try {
        const content = await fs.promises.readFile(filePath)
        res.writeHead(200, { 'Content-Type': type })
        res.end(content, 'utf-8')
    } catch (error) {
        res.writeHead(['ENOENT', 'EISDIR'].includes(error.code) ? 404 : 500)
        res.end()
    }
}

const server = http.createServer(handler)
server.listen(3000)
