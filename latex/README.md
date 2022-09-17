# LaTex常见语法记录
- 无编号分点
~~~
\begin{enumerate}
	\item 
	\item 
	\item 
\end{enumerate}
~~~
- 有编号分点
~~~
\begin{itemize}
	\item
	\item 
	\item 
\end{itemize}
~~~
- 图像引入与引用
~~~
\begin{figure}[!h]
	\centering
	\includegraphics[width=.85\textwidth]{P1}
	\caption{图片示意}
	\label{P1}
\end{figure}

\ref{P1}
~~~
- 表格表头添加
~~~
\begin{table}[!h]
	\centering
	\caption[fh]{符号说明表}
	\label{fuhao}
~~~
- 引用python语法（提前加入配置文件）
~~~
\begin{python}

\end{python}
~~~