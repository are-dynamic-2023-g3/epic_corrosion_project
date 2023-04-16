# corrosion_project

La formation de la rouille sur le fer est un processus chimique qui se produit lorsque le fer réagit avec l'oxygène et l'eau. Afin de modéliser ce processus, nous avons commencé par établir une fonction "Rusting" qui prend en paramètres les concentrations de fer, d'ions Fe2+, d'oxygène et d'eau, ainsi que deux constantes de vitesse.

Nous avons utilisé les formules des réactions anodique et cathodique :

<img width="282" alt="image" src="https://user-images.githubusercontent.com/125261904/231500682-3cf1d9dc-0adb-420d-b6e5-d57ffa3c1a9e.png">

![download](https://user-images.githubusercontent.com/125261904/232252157-41356db6-7a67-41fb-b3bb-2fa0b11068d0.png)

Notre fonction calcule la vitesse de la réaction anodique qui convertit le fer en ions Fe2+ en présence d'eau en utilisant l'équation suivante :

 r_anodic = k1 * iron * oxygen**(1/2) * (1 - fe2/iron)
 
 k1:une constante de vitesse.
 
La fonction calcule ensuite la vitesse de la réaction cathodique qui convertit l'oxygène et l'eau en ions d'hydroxyde en présence d'ions Fe2+, en utilisant l'équation suivante :
 
 r_cathodic = k2 * oxygen * water**(1/2) * (1 - fe2/iron)
  
 k2: une autre constante de vitesse.
  
La fonction utilise ces vitesses de réaction pour calculer le changement de concentration de fer, d'ions Fe2+, d'oxygène et d'eau au fil du temps.

Les conditions initiales sont :

 concentration de fer = 1 mol/m^3

 concentration des ions Fe2+ = 0 mol/m^3

 concentration d'oxygène = 1 mol/m^3

 concentration d'eau = 0 mol/m^3

avec les constantes de vitesse de 0.01 et 0.02, respectivement.
  
  ![download](https://user-images.githubusercontent.com/125261904/232252188-b607bc2f-a471-4902-8e6d-6109e88e00d9.png)

  Avec les constantes de vitesse de 0.08 et 0.06 respectivement:
  
  ![download](https://user-images.githubusercontent.com/125261904/232252166-198311ef-5483-49f8-8ca0-1be5f8496285.png)

  En modifiant la concentration d'eau à 0,5 mol/m^3, on obtient :
  
  
  ![download](https://user-images.githubusercontent.com/125261904/232252210-30e802cb-b45a-43d5-be14-f7f7b26d4335.png)
  

On a voulu étudier le changement de concentration d'oxygène et de rouille à partir d'une réaction électrochimique appelée réaction de Butler-Volmer.

Pour cela, on a utilisé les taux de réaction anodique et cathodique en calculant leurs potentiels d'équilibre avec les formules suivantes :
 
<img width="409" alt="image" src="https://user-images.githubusercontent.com/125261904/231562591-96aefb22-2271-4c0c-82f6-5d07c165bb87.png">

La simulation est effectuée en utilisant la fonction solve_ivp de NumPy pour résoudre les équations différentielles, et les résultats sont tracés à l'aide de Matplotlib.

En initialisant les concentrations de l'oxygène, de la rouille et de l'eau à 1 mol/m^3, 0 mol/m^3 et à 55,5 mol/m^3, respectivement, et en mettant la température à 298 K, on obtient ces graphes :


  ![download](https://user-images.githubusercontent.com/125261904/231439849-4817d0e2-c67e-4732-a0de-d21e1122680c.png)
  
 En mettant la concentration l'oxygène à 3 mol/m^3 ,on a :

![download](https://user-images.githubusercontent.com/125261904/232291067-86a62de4-7972-4f96-a4cc-1f611073c22f.png)

 En augmentant la température jusqu'à 323 K, on a :
 
  ![download](https://user-images.githubusercontent.com/125261904/232295759-f50a1cf6-a633-4b6b-a690-a1c216689d7e.png)

On a aussi tracé les densités de courant anodique et cathodique en fonction du potentiel :

![download](https://user-images.githubusercontent.com/125261904/231443740-377d8d90-343a-41b5-a0f6-7351ba59b245.png)


  
 D’après les graphes précédents, nous remarquons qu’augmenter la concentrations de différents facteurs et changer les conditions environnementales initiales a un fort impact sur la vitesse du processus de corrosion.

On en déduit donc que plus la température et la concentration d’oxygène et d’eau sont élevées, plus la rouille se forme rapidement.

  
  
  
  
   
   
   
  
  

  
  
  
  
