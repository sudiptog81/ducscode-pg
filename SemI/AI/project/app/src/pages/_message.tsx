import styles from '@/styles/Chat.module.css'

export default function Message ({ message }) {
  return (
    <div className={styles.message}>
      <span className={styles.messageAuthor}>{message.author}</span>
      <span>{message.content}</span>
    </div>
  )
}
