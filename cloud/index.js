const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 80;
app.use(express.static('public'))

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'public/uploads/')
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname))
    }
});

const upload = multer({
    storage,
    limits: { fileSize: 10 * 1024 * 1024 * 1024 }, // 10 GB limit
    fileFilter: (req, file, cb) => {
        const ext = path.extname(file.originalname).toLowerCase()
        if (ext != ".png" && ext != ".jpg" && ext != ".jpeg") {
            return cb(new Error('Only .png, .jpg and .jpeg files are allowed'))
        }
        cb(null, true);
    }
})

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html')
})

app.post('/upload', upload.single('file'), (req, res) => {
    const ext = path.extname(req.file.originalname).toLowerCase();
    console.log(ext)
    if (!req.file) {
        return res.status(400).send('No file uploaded')
    }
    res.json({ 
        message: 'File uploaded successfully',
        filename: req.file.filename,
        path: req.file.path
    })
})

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`)
})