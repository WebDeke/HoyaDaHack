import Head from "next/head";
import { useState } from "react";
import styles from "./index.module.css";

export default function Home() {
  const [taskInput, setTaskInput] = useState("");
  const [result, setResult] = useState();

  async function onSubmit(event) {
    event.preventDefault();
    try {
      const response = await fetch("/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ task: taskInput }),
      });

      const data = await response.json();
      if (response.status !== 200) {
        throw (
          data.error ||
          new Error(`Request failed with status ${response.status}`)
        );
      }

      setResult(data.result);
      setTaskInput("");
    } catch (error) {
      // Consider implementing your own error handling logic here
      console.error(error);
      alert(error.message);
    }
  }

  return (
    <div>
      <Head>
        <title>To-Do Lister</title>
        <link rel="icon" href="/dog.png" />
      </Head>

      <main className={styles.main}>
        <img src="/dog.png" className={styles.icon} />
        <h3>Name my task</h3>
        <form onSubmit={onSubmit}>
          <input
            type="text"
            name="task"
            placeholder="Enter a task"
            value={taskInput}
            onChange={(e) => setTaskInput(e.target.value)}
          />
          <input type="submit" value="Break my tasks down" />
        </form>
        <div className={styles.result}>{result}</div>
      </main>
    </div>
  );
}
