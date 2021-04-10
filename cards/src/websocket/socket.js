import { io } from "socket.io-client"

const url = 'ws://0.0.0.0:8080'

export const socket = io(url)

