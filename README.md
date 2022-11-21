# 網路程式設計

## Lab 8 – Non-blocking Socket

本作業請設計一個 Server 及兩個 Clients  (Producer 與 Consumer)，這三個程式的功能如下：

**Server**

<ol>
    <li>同時註冊兩個 port numbers 並維護一個長度為 5 的整數的佇列 (Queue)。</li>
    <li>註冊到port number 8880的連線負責接收 Producer 所傳來的訊息(其型態為整數)；當 Server 收到訊息後會將收到的整數加入 Queue 中，如果 Queue 已滿，Server 會回傳一個 Error message 給 Producer。</li>
    <li>註冊到port number 8881的連線負責處理 Consumer 的要求，當 Server 收到 Consumer 的要求後會從 Queue 中取出一個整數並回傳給 Consumer。當 Queue 中沒有資料時，Consumer 與 Server 之間的連線將持續，直到 Server 的 Queue 中有資料 Server 才回傳。</li>
    <li>Server 可以同時處理多個 Consumers / Producers 的連線要求(即可能有兩個以上的 Producers 會送資料給 Server，兩個以上的 Consumers 同時從 Server 取資料)。</li>
</ol>



**Producer**

提供一個使用者介面讓使用者可以輸入一個整數，並將這一個整數傳送到 Server 中 (以 port number 8880)；傳送後 Producer 會顯示所傳送的資料是否已成功加入 Server 的 Queue 中。

**Consumer**

執行後會發出一個要求到 Server 的 8881 port，等待接收Server 所回傳的整數並顯示出來。如果Queue 中沒有資料， Consumer 在等待時會每隔2秒秀出一個”資料等待中”的訊息