//
//  ViewController.m
//  Calculator
//
//  Created by Bihany, Tushar on 1/12/17.
//  Copyright © 2017 Bihany, Tushar. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    inputstring = [[NSString alloc]init];
    operand1 = [[NSString alloc]init];
    operand2 = [[NSString alloc]init];
    operation = [[NSString alloc] init];

    [super viewDidLoad];
    // Do view setup here.
}

-(IBAction)digits:(NSButton *)sender
{
    switch (sender.tag)
    {
        case 0:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"0"];
            result.stringValue = inputstring;
            break;
            
        case 1:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"1"];
            result.stringValue = inputstring;
            break;
            
        case 2:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"2"];
            result.stringValue = inputstring;
            break;
            
        case 3:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"3"];
            result.stringValue = inputstring;
            break;
            
        case 4:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"4"];
            result.stringValue = inputstring;
            break;
            
        case 5:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"5"];
            result.stringValue = inputstring;
            break;
            
        case 6:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"6"];
            result.stringValue = inputstring;
            break;
            
        case 7:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"7"];
            result.stringValue = inputstring;
            break;
            
        case 8:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"8"];
            result.stringValue = inputstring;
            break;
            
        case 9:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"9"];
            result.stringValue = inputstring;
            break;
            
        case 10:
            inputstring = [NSString stringWithFormat: @"%@%@",inputstring, @"."];
            result.stringValue = inputstring;
            break;
            
        case 11:
            operand1 = inputstring;
            inputstring = @"";
            operation = @"+";
            result.stringValue = operation;
            break;
            
        case 12:
            operand1 = inputstring;
            inputstring =@"";
            operation = @"-";
            result.stringValue = operation;
            break;
            
        case 13:
            operand1 = inputstring;
            inputstring =@"";
            operation = @"*";
            result.stringValue = operation;
            break;
            
        case 14:
            operand1 = inputstring;
            inputstring =@"";
            operation = @"/";
            result.stringValue = operation;
            break;
            
        case 15:
            operand1 = inputstring;
            inputstring =@"";
            operation = @"%";
            result.stringValue = operation;
            break;
            
        case 16:
            operand1 = @"";
            inputstring =@"";
            operation = @"";
            operand2 = @"";
            result.stringValue = @"";
            break;
            
        case 17:
            operand2 = inputstring;
            
            if ([operation  isEqual: @"+"]) {
                result.stringValue = [NSString stringWithFormat: @"%lf", [operand1 doubleValue]+ [operand2 doubleValue]];

            }
            
            if ([operation  isEqual: @"-"]) {
                result.stringValue = [NSString stringWithFormat: @"%lf", [operand1 doubleValue] - [operand2 doubleValue]];
                
            }
            
            if ([operation  isEqual: @"*"]) {
                result.stringValue = [NSString stringWithFormat: @"%lf", [operand1 doubleValue] * [operand2 doubleValue]];
                
            }
            
            if ([operation  isEqual: @"/"]) {
                result.stringValue = [NSString stringWithFormat: @"%lf", [operand1 doubleValue] / [operand2 doubleValue]];
                
            }
                 
            if ([operation  isEqual: @"%"]) {
                     result.stringValue = [NSString stringWithFormat: @"%ld", [operand1 integerValue] % [operand2 integerValue]];
                     
                 }
            
            inputstring =@"";
            operation = @"";
            operand2 = @"";
            operand1 = @"";
            
            break;
            
        default:
            break;
    }
}

@end
