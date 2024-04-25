// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-analytics.js";
import {
    getFirestore, collection, getDocs
} from 'https://www.gstatic.com/firebasejs/10.10.0/firebase-firestore-lite.js';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyA533wgBVqv287VTlHQX9xN3m6qcQZm3x4",
    authDomain: "articulating-7a9e1.firebaseapp.com",
    projectId: "articulating-7a9e1",
    storageBucket: "articulating-7a9e1.appspot.com",
    messagingSenderId: "949118825714",
    appId: "1:949118825714:web:2af7e253d9ac2d04f00c6b",
    measurementId: "G-X280BQ128J"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

