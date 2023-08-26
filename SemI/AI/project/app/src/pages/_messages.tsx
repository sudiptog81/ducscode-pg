import styles from '@/styles/Chat.module.css'
import { Key } from 'react'
import Message from './_message'

export default function Messages ({ messages, setMessages }) {
  return (
    <div className={styles.messages}>
      {messages.map((message: any, index: Key) => (
        <Message key={index} message={message} />
      ))}
    </div>
  )
}
