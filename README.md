# jokes
joke client and server <br>
![image](https://user-images.githubusercontent.com/5352741/236083193-e1aa0b77-d6f5-4bbf-9723-60955be82a66.png)
<br>
joke data is from https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes?resource=download



<h2>Dockerfile:<br></h2>

\# port 65433<br>
FROM  python:latest<br>
COPY shortjokes.txt /shortjokes.txt <br>
COPY jokes.py /jokes.py<br>
EXPOSE 65433<br>
CMD /jokes.py<br>
