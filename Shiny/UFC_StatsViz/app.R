
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)
library(tidyverse)
library(plotly)
library(reshape2)
library(DT)
library(crosstalk)

ufc <- read_csv("UFC_Stats_final.csv")

ufc5 <- ufc %>%
  group_by(fightGender, Division, bC_Name) %>% 
  select("fightGender", "Division","Name" = "bC_Name", "SLpM" = "bC_SLpM", "StrAcc" = "bC_StrAcc", 
         "SApM" = "bC_SApM", "StrDef" = "bC_StrDef", "SigStrDif" = "bC_SigStrDif", "TDAcc" = "bC_TDAcc", "TDDef" = "bC_TDDef",
         "ttlFightTime")

ufc6 <- ufc %>%
  group_by(fightGender, Division, rC_Name) %>% 
  select("fightGender", "Division","Name" = "rC_Name", "SLpM" = "rC_SLpM", "StrAcc" = "rC_StrAcc", 
         "SApM" = "rC_SApM", "StrDef" = "rC_StrDef", "SigStrDif" = "rC_SigStrDif", "TDAcc" = "rC_TDAcc", "TDDef" = "rC_TDDef",
         "ttlFightTime")

ufcFinal <- bind_rows(ufc5, ufc6)  %>%
  group_by(fightGender, Division, Name) %>%
  summarise(SLpM = mean(SLpM), StrAcc = mean(StrAcc), SApM = mean(SApM), StrDef = mean(StrDef), SigStrDif = sum(SigStrDif), 
            TDAcc = mean(TDAcc), TDDef = mean(TDDef), ttlFightTime = sum(ttlFightTime), ttlRounds = (ttlFightTime/5))


# Define UI for application that draws a histogram
ui <- dashboardPage(skin = "red",
  dashboardHeader(title = "UFC Stats"),
  dashboardSidebar(
    sidebarMenu(id = "tabs",
                menuItem("Home", tabName = "Home", icon = icon("home")),
                menuItem("Results by Division", tabName = "ResultsByDivision", icon = icon("poll")),
                menuItem("Stat Leaders", tabName = "StatLeaders", icon = icon("signal")),
                menuItem("Fighter Lookup", tabName = "fighterSearch", icon = icon("search")),
                menuItem("Source code", icon = icon("file-code-o"), 
                         href = "https://github.com/rstudio/shinydashboard/")
    )
  ),
  dashboardBody(
    tabItems(
      tabItem(tabName = "Home", h1("Home"),
              fluidRow(
                box(
                  width = 12,
                  p("Welcome to the first and only shiny app that displays up to date UFC stats as provided by FightMetrix, 
                    a subsidiary of the Ultimate Fighting Championship"),
                  p("The information, statistics, and visualizations contained in this app are derived from a webscrape of UFCstats.com. 
                     A single database containing  4,820 observations of 333 unique variables in relation to individual fights was compiled 
                     using scrapy for python. Further research will be conducted to compile even more information from various sources 
                     to enhance the user experience and breadth of knowledge available for fight analysis. If you have any questions, 
                     concerns, comments, or suggestions feel free to contact me directly at", tags$a(href="camwisdom@pm.me", "camwisdom@pm.me"), "!")
                ),
                box(
                  width = 12,
                  tags$iframe(src = "https://www.youtube.com/embed/GB5dnA9GRF0",width = 1740,height=680, align = "center")
                ),
                box(
                  width = 12,
                  tags$h3("Purpose:"),
                  p("The main purpose of compiling the dataset that serves this app was to enhance the internal operations of the business 
                    and user experience for the consumer. Mixed Martial Arts is still a young and relatively niche offering when compared 
                    to the audience reach of more mature and well-established sports. The UFC only gained traction just outside the mainstream
                    sports audience in April 2005, when the first season of its wildly popular “The Ultimate Fighter” reality series aired its
                    finale on a free cable broadcast in the United States. "),
                  p("In the company’s infancy, the gathering of relevant data pertaining to the performance of its athlete’s was sparse and much 
                    of the information is incomplete. Over the last 14 years, the data gathered and processed has increased in breadth and completeness 
                    but lacks the infrastructure to promote painless dissemination to a variety of downstream consumers. "
                  ),
                  p("More recently, many of the athlete’s that helped the UFC enter the mainstream in the early 2010’s have since retired or seemingly 
                    priced themselves out of competition for the promotion. Brock Lesnar, Conor McGregor, and Ronda Rousey account for 9 of the top 10
                    highest-selling Pay Per Views of all time. This is not to say that the level of talent or competition has dropped in recent years. 
                    In fact, the argument can be made that the promotion’s talent has never been as skilled or deeply competitive as its current iteration. 
                    The most recent PPV, one that was stacked in terms of highly competitive matchups, sold less than 120,000 units due to a combination of factors."
                  ),
                  p("The UFC has a talent development issue. If they continue to fail in developing talent that can cross over into mainstream appeal, they will struggle 
                    to grow and attract new audiences. They can utilize data currently available to them to enhance their marketing and advertising, social media presence 
                    of the promotion and it’s talent, talent evaluation and scouting and so much more. The beta version of this dataset attempts to begin to explore currently 
                    available public data to resolve these issues with actionable insights."
                  )
                )
              )
      ),
      tabItem(tabName = "ResultsByDivision", h1("Fight Results by Division"),
              fluidRow(
                column(4, selectInput("Gender", h3("Select Gender"), 
                            choices = list("Men's" = "Men's", "Women's" = "Women's"), 
                            selected = "Men's")),
                column(8, 
                infoBoxOutput("fightCountBox"),
                infoBoxOutput("finishes"),
                infoBoxOutput("goTheDistance")
              )),
              fluidRow(
                plotlyOutput("divResultsBar")
              ),
              fluidRow(
                plotlyOutput("divResultsBarPerc")
              )
      ),
      tabItem(tabName = "StatLeaders", h1("Stat Leaders"),
              fluidRow(
                column(2, selectInput("StatGender", h4("Select Gender"), 
                            choices = list("Men's" = "Men's", "Women's" = "Women's"), 
                            selected = "Men's")),
                column(2, selectInput("Division", h4("Select Division"), 
                            choices = list("Heavyweight" = "Heavyweight", "Light Heavyweight" = "Light Heavyweight",
                                           "Middleweight" = "Middleweight", "Welterweight" = "Welterweight", 
                                           "Lightweight" = "Lightweight", "Featherweight" = "Featherweight",
                                           "Bantamweight" = "Bantamweight", "Flyweight" = "Flyweight", "Strawweight" = "Strawweight"), 
                            selected = "Featherweight")),
                column(2, selectInput("Stat", h4("Select Stat"), 
                            choices = list("Significant Strikes Landed per Minute" = "SLpM", 
                                           "Significant Striking Accuracy" = "StrAcc",
                                           "Significant Strikes Absorbed per Minute" = "SApM", 
                                           "Significant Striking Defensive %" = "StrDef",
                                           "Significant Striking Differential" = "SigStrDif",
                                           "Takedown Accuracy" = "TDAcc", 
                                           "Takedown Defense" = "TDDef")), 
                            selected = "SLpM"),
                column(3, sliderInput("topNSlider", h4("# of Fighters to Display"),
                            min = 3, max = 15, value = 9)),
                
                column(3, sliderInput("numFightSlider", h4("Filter minimum # of fights to be eligible"),
                          min = 1, max = 15, value = 5))
              
              ),
              fluidRow(
                plotlyOutput("statLeadersBar")
              )
      ),
      tabItem(tabName = "fighterSearch", h1("Fighter Lookup"),
              fluidRow(

                ),
              fluidRow(
                box(
                  width = 12,
                  plotlyOutput("x2"),
                  DT::dataTableOutput("x1"))
                  
                )
              )
          )  
    )
  )




# Define server logic required to draw a histogram
server <- function(input, output) {
  
orderedDivs <-  c("Catch Weight", "Heavyweight", "Light Heavyweight", "Middleweight", 
                  "Welterweight", "Lightweight", "Featherweight",
                  "Bantamweight", "Flyweight", "Strawweight")
  
  
  divResultsDF <- reactive({
    ufc %>% 
      filter(fightGender == input$Gender)
  })
  
  output$fightCountBox <- renderValueBox({
    df <- divResultsDF()
    
    countrows <- nrow(df)
    
    valueBox(
      paste0(countrows), "Total Fights", icon = icon("hashtag"),
      color = "red"
    )
  })
  
  output$goTheDistance <- renderValueBox({
    
    dfFull <- divResultsDF()
    
    fullRows <- nrow(dfFull)
    
    
    dfFilt <- divResultsDF() %>%
        mutate(methodClean = ifelse(grepl("Unanimous", method, fixed = TRUE), "Decision - Unanimous", 
                                  ifelse(grepl("KO", method, fixed =  TRUE), "KO/TKO",
                                         ifelse(grepl("Submission", method, fixed = TRUE), "Submission",
                                                ifelse(grepl("Split", method, fixed = TRUE), "Decision - Split", "Other"))))) %>%
       group_by(Division) %>% 
       filter(methodClean == "Decision - Split" | methodClean ==  "Decision - Unanimous")
    
    filtRows <- nrow(dfFilt)
    
    valueBox(
      paste0( round(((filtRows/fullRows)*100), 0), "%"), "of all fights go to a judges decision", icon = icon("percentage"),
      color = "red"
    )
  })
  
  output$finishes <- renderValueBox({
    df <- divResultsDF() %>%
      mutate(methodClean = ifelse(grepl("Unanimous", method, fixed = TRUE), "Decision - Unanimous", 
                                  ifelse(grepl("KO", method, fixed =  TRUE), "KO/TKO",
                                         ifelse(grepl("Submission", method, fixed = TRUE), "Submission",
                                                ifelse(grepl("Split", method, fixed = TRUE), "Decision - Split", "Other"))))) %>%
      group_by(Division) %>% 
      filter(methodClean == "KO/TKO" | methodClean == "Submission")
    
    countrows <- nrow(df)
    
    valueBox(
      paste0(countrows), " # of Fights ending in a finish", icon = icon("exclamation"),
      color = "red"
    )
  })
  

  
  output$divResultsBar <- renderPlotly({
    ufcPlot <- divResultsDF() %>%
      ggplot(aes(x=factor(Division, levels = orderedDivs))) +
      geom_bar(aes(fill = method)) +
      labs(x = "Division", y = "Fight Count", fill = "Result")
    
    ufcPlotly <- ggplotly(ufcPlot)
  })
  
  output$divResultsBarPerc <- renderPlotly({
    ufcData<- divResultsDF() %>%
      mutate(methodClean = ifelse(grepl("Unanimous", method, fixed = TRUE), "Decision - Unanimous", 
                                  ifelse(grepl("KO", method, fixed =  TRUE), "KO/TKO",
                                         ifelse(grepl("Submission", method, fixed = TRUE), "Submission",
                                                ifelse(grepl("Split", method, fixed = TRUE), "Decision - Split", "Other"))))) %>%
      group_by(Division)
    
    ufcLabs <- divResultsDF() %>%
      mutate(methodClean = ifelse(grepl("Unanimous", method, fixed = TRUE), "Decision - Unanimous", 
                                  ifelse(grepl("KO", method, fixed =  TRUE), "KO/TKO",
                                         ifelse(grepl("Submission", method, fixed = TRUE), "Submission",
                                                ifelse(grepl("Split", method, fixed = TRUE), "Decision - Split", "Other"))))) %>%
      group_by(Division) %>% 
      count(methodClean) %>%
      mutate(ratio = scales::percent(n/sum(n)))
      
    ufcPlot <- ufcData %>%   
      ggplot(aes(x=factor(Division, levels = orderedDivs), fill = factor(methodClean))) +
      geom_bar(position = "fill") +
      labs(x = "Division", y = "Percentage of total division fights", fill = "Result") +
      geom_text(data=ufcLabs, aes(y=n,label=ratio),
                position=position_fill(vjust=0.5))

    ufcPlotlyPerc <- ggplotly(ufcPlot)
  })
  
  statLeaders_bC <- reactive({
    ufc %>% 
      filter(fightGender == input$StatGender & Division == input$Division & ttlFightTime >= 1) %>% 
      group_by(fightGender, Division, bC_Name) %>% 
      select("fightGender", "Division","Name" = "bC_Name", "SLpM" = "bC_SLpM", "StrAcc" = "bC_StrAcc", 
             "SApM" = "bC_SApM", "StrDef" = "bC_StrDef", "SigStrDif" = "bC_SigStrDif", "TDAcc" = "bC_TDAcc", "TDDef" = "bC_TDDef",
             "ttlFightTime")
  })
  
  statLeaders_rC <- reactive({
    ufc %>% 
      filter(fightGender == input$StatGender & Division == input$Division & ttlFightTime >= 1) %>% 
      group_by(fightGender, Division, rC_Name) %>% 
      select("fightGender", "Division","Name" = "rC_Name", "SLpM" = "rC_SLpM", "StrAcc" = "rC_StrAcc", 
             "SApM" = "rC_SApM", "StrDef" = "rC_StrDef", "SigStrDif" = "rC_SigStrDif", "TDAcc" = "rC_TDAcc", "TDDef" = "rC_TDDef",
             "ttlFightTime") 
  })
  
  output$statLeadersBar <- renderPlotly({

    blue <- statLeaders_bC()
    red <- statLeaders_rC()
    
    combined <- bind_rows(blue, red) 
    
    avg = round(mean(combined$mean), 3)
    
    
    fightCountdf <- as.data.frame(table(combined$Name))
    
    combined <- combined %>%
                  group_by(Name) %>%
                  summarise(mean = mean(!! rlang::sym(input$Stat)))
    
    
    combined$numFights <- fightCountdf$Freq
    
    
    combinedFilt <- combined %>% 
              filter(numFights >= input$numFightSlider)
    
    df <- combinedFilt %>%
            arrange(desc(mean))
    
    
    dfCalc <- df %>% 
              top_n(input$topNSlider)
    
    
    statLeaderPlot <- dfCalc %>% 
                  ggplot(aes(x = reorder(Name, -mean), y = mean)) +
                  geom_bar(stat = "identity", fill = "#b20101") +
                  geom_hline(yintercept=avg, linetype="dashed", color = "white") +
                  geom_text(aes(label= round(mean, digits = 3), color = "#FFFFFF"), position=position_stack(vjust=.5)) +
                  labs(x = "Fighter Name", y = "Value") +
                  theme(legend.position="none")
      
    
    statLeaderPlotly <- ggplotly(statLeaderPlot)
  })
  
  
  d <- SharedData$new(ufcFinal, ~Name)
  
  # highlight selected rows in the scatterplot
  output$x2 <- renderPlotly({
    
    s <- input$x1_rows_selected
    
    if (!length(s)) {
      p <- d %>%
        plot_ly(x = ~SLpM, y = ~StrAcc, mode = "markers", color = I('black'), name = 'Unfiltered') %>%
        layout(showlegend = T) %>% 
        highlight("plotly_selected", color = I('red'), selected = attrs_selected(name = 'Filtered'))
    } else if (length(s)) {
      pp <- ufcFinal %>%
        plot_ly() %>% 
        add_trace(x = ~SLpM, y = ~StrAcc, mode = "markers", color = I('black'), name = 'Unfiltered') %>%
        layout(showlegend = T)
      
      # selected data
      pp <- add_trace(pp, data = ufcFinal[s, , drop = F], x = ~SLpM, y = ~StrAcc, mode = "markers",
                      color = I('red'), name = 'Filtered')
    }
    
  })
  
  # highlight selected rows in the table
  output$x1 <- DT::renderDataTable({
    ufcFinal2 <- ufcFinal[d$selection(),]
    dt <- DT::datatable(ufcFinal)
    if (NROW(ufcFinal2) == 0) {
      dt
    } else {
      DT::formatStyle(dt, "Name", target = "row",
                      color = DT::styleEqual(ufcFinal2$Name, rep("white", length(ufcFinal2$Name))),
                      backgroundColor = DT::styleEqual(ufcFinal2$Name, rep("black", length(ufcFinal2$Name))))
    }
  })
  

  

}

# Run the application 
shinyApp(ui = ui, server = server)



